#Vue with axios
````
#For more information can check this url
https://axios-http.com/docs/intro

#CDN
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

#Add to vue instan
mounted() {
    axios.get('http://127.0.0.1:5000/get_all_product')
    .then(response => {
        this.product_list = response.data
        $.LoadingOverlay("hide");
    })
}


````

````
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-loading-overlay/2.1.7/loadingoverlay.min.js"></script>
````
