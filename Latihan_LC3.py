from fastapi import FastAPI, HTTPException, Header
import pandas as pd

#create instance/object
app = FastAPI()
apiKey = "latihanlc3"

#membaca data yang sudah dihandle outlier
data = pd.read_csv("handled_data.csv")

@app.get("/")
def user_interface():
    return {"message": "Halo, ini Latihan LC3"}

#endpoint untuk menampilkan seluruh data setelah penanganan outlier
@app.get("/data")
def all_data():
    data_dict = data.to_dict(orient='records')
    return {"data": data_dict}

#endpoint untuk menampilkan data berdasarkan index
@app.get("/data/{id}")
def data_by_index(id: int):

    if id < 0 or id > len(data):
        raise HTTPException(status_code=404, detail='Data tidak ditemukan')
    row = data.iloc[id]
    # else:
    return {"data": row.to_dict()}
    # data.to_dict(orient='records')

print(data.head())

#endpoint untuk menghapus data berdasarkan index
@app.delete("/delete/{index}")
def delete_data(index: int):
    data = pd.read_csv("handled_data.csv")
    #mengecek apakah index valid
    #mengecek index sebelum dihapus
    print(f"Jumlah data sebelum penghapusan: {len(data)}")

    if index < 0 or index >= len(data):
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    
    #menghapus entry data dari DataFrame
    
    data = data.drop(data.index[index])
    data.reset_index(drop=True,inplace=True)

    #mengembalikan peubahan ke file csv
    data.to_csv("handled_data.csv", index=False)
    return {"message": "Data berhasil dihapuskan", "index": index}