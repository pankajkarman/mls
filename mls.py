import requests, os
from tqdm import tqdm

class MLSDownload:
    def __init__(self, filename, skiprows=2):
        self.filename = filename
        self.skiprows = skiprows
        with open(filename, "r") as f:
            lines = f.readlines()[skiprows:]
            lines = [line.strip() for line in lines]
        self.links = lines

    def download(self, odir="./data/mls/"):
        desc = self.filename.split('_')[1]
        for infile in tqdm(self.links, desc=desc):
            fname = infile.split("/")[-1]
            species = fname.split("-")[2].split("_")[0].lower()
            filename = odir + species + "/" + fname
            if not os.path.exists(filename):
                resp = requests.get(infile)
                with open(filename, "wb+") as f:
                    f.write(resp.content)
