import os
from datetime import datetime, timedelta
from tqdm import tqdm
import copernicusmarine as cm
from copernicusmarine import open_dataset, login
import concurrent.futures

# Identifiants CMEMS (remplis une fois)
cm.login(username="usrname", password="psswd") 

# Paramètres
dataset_id = "cmems_mod_glo_phy_my_0.083deg_P1D-m"
root_path = "/mnt/data/jmv/Unilasalle/datacopernicus/"
name = "glorys12_1day"
variables = ["thetao"]
min_lon, max_lon = -40,-30
min_lat, max_lat = -40,-30
start_date = datetime.strptime("1993-03-18", "%Y-%m-%d")
end_date = datetime.strptime("2024-01-03", "%Y-%m-%d")
max_workers = 10  # Tu peux l'augmenter si ton réseau/machine le supporte

# Créer le dossier s'il n'existe pas
os.makedirs(root_path, exist_ok=True)

# Génère la liste des dates
all_dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Log d'erreurs
errors = []
lock = tqdm.get_lock()  # Pour éviter les conflits de tqdm entre threads

# Fonction de téléchargement par jour
def download_day(date_obj):
    date_str = date_obj.strftime("%Y-%m-%d")
    filename = f"{name}_{date_str}.nc"
    save_path = os.path.join(root_path, filename)

    if os.path.exists(save_path):
        return  # Déjà téléchargé

    try:
        ds = open_dataset(
            dataset_id=dataset_id,
            minimum_longitude=min_lon,
            maximum_longitude=max_lon,
            minimum_latitude=min_lat,
            maximum_latitude=max_lat,
            variables=variables,
            start_datetime=date_str,
            end_datetime=date_str,
        )
        ds.to_netcdf(save_path)
    except Exception as e:
        errors.append((date_str, str(e)))

# Lancement multithread
with tqdm(total=len(all_dates), desc="Téléchargement multi-thread") as pbar:
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(download_day, date): date for date in all_dates}
        for future in concurrent.futures.as_completed(futures):
            pbar.update(1)

# Log des erreurs
if errors:
    log_path = os.path.join(root_path, "download_errors_multithread.log")
    with open(log_path, "w") as f:
        for date_str, err in errors:
            f.write(f"{date_str}: {err}\n")
    print(f"{len(errors)} erreurs rencontrées. Voir {log_path}")
else:
    print("Fin du téléchargement, pas d'erreurs rencontrées.")

