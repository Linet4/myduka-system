let modal = document.getElementById("myModal");
let btn = document.getElementById("myBtn");
let span = document.getElementsByClassName("close")[0];
btn.onclick = function() {
    modal.style.display = "block";
  }
  span.onclick = function() {
    modal.style.display = "none";
  }
  
let form=document.getElementsByName("myform")

form.addEventListener('submit',function(e){
    // prevent the page from refreshing
    e.preventDefault()
    let product_name=document.getElementsByName("product_name").value
})