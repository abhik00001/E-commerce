var updatebtns = document.getElementsByClassName("update-cart");

for (i = 0; i < updatebtns.length; i++) {
    // add click event listener for each button 
    updatebtns[i].addEventListener('click', function () {
        let productID = this.dataset.product;
        let action = this.dataset.action;
        console.log("ProductID: " + productID + ", Action: " + action);
        console.log("USER:", user)
        if (user == 'AnonymousUser') {
            alert("You must be logged in to perform that action.")
        }
        else {
          updateUserOrder(productID , action)
        };
    })
};

function updateUserOrder(productId, action){
    console.log("User is authenticated , sending data...")
    let url = "/addItem/"
    fetch (
        url,{
            method:"POST",
            headers:{
                'Content-Tpye':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({"productId":productId,"action":action})
        })
        .then ((response) =>{
            return response.json();
        })
        .then((data)=>{
            console.log("data :", data),
            location.replace("/cart/")
        }); 
}


