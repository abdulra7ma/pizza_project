const header = document.querySelector('.header');

window.addEventListener('scroll', function() {
    if (window.pageYOffset > 0) {
        header.classList.add('header_scrolled');
    } else {
        header.classList.remove('header_scrolled');
    }
});

// document.getElementById("add-to-cart").addEventListener("click", function() {
//     // Add code here to add the item to the cart
// });

// Get all the plus and minus buttons
const minusButtons = document.querySelectorAll(".grid_minus");
const plusButtons = document.querySelectorAll(".grid_plus");

// Add click event listeners to each button
minusButtons.forEach((button) => {
    button.addEventListener("click", decreaseQuantity);
});

plusButtons.forEach((button) => {
    button.addEventListener("click", increaseQuantity);
});

// Function to decrease the quantity
function decreaseQuantity(event) {
    const quantityElement = event.target.nextElementSibling;
    const element_price = parseFloat(quantityElement.getAttribute("price"));
    let quantity = parseInt(quantityElement.innerText);

    if (quantity > 0) {
        quantity--;
        quantityElement.innerText = quantity;
        decreaseTotal(element_price);
    }
}

function formatNumber(num) {
  if (num % 1 !== 0) {
    return num.toFixed(2);
  } else {
    return num + ".00";
  }
}

// Function to increase the quantity
function increaseQuantity(event) {
    const quantityElement = event.target.previousElementSibling;
    const element_price = parseFloat(quantityElement.getAttribute("price"));
    let quantity = parseInt(quantityElement.innerText);

    quantity++;
    quantityElement.innerText = quantity;
    increaseTotal(element_price);
}

function increaseTotal(amount) {
    const totalElement = document.querySelector("#total-price");
    const match = totalElement.innerText.match(/\d+(\.\d+)?/);
    const total = match ? parseFloat(match[0]) : 0;
    const new_amount = total + amount;
    totalElement.innerText = `Total: $${formatNumber(new_amount)}`;
}

function decreaseTotal(amount) {
    const totalElement = document.querySelector("#total-price");
    const match = totalElement.innerText.match(/\d+(\.\d+)?/);
    const total = match ? parseFloat(match[0]) : 0;
    const new_amount = total - amount;
    totalElement.innerText = `Total: ${new_amount}`;
}