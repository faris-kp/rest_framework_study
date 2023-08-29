import requests


product_id = input("What is the product id you want use\n")
try: 
    product_id = int(product_id)
except:
    product_id= None
    print(f'{product_id} not a valide')
    
if product_id:

    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_responce = requests.delete(endpoint)



    print("statuscoe",get_responce.status_code)
    
    print("204",get_responce.status_code==204)
