async function postJSON(url, data){
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': window.csrfToken,
    },
    body: JSON.stringify(data),
  });
  return await res.json();
}

function addToCart(productId){
  postJSON('/cart/add/', {product_id: productId, quantity: 1})
    .then(r => {
      if(!r.ok){ alert(r.error || 'Failed'); return; }
      alert('Added to cart');
    })
    .catch(()=>alert('Failed to add'));
}

function updateQty(productId, delta){
  const row = document.querySelector(`.cart-row[data-product-id="${productId}"]`);
  if(!row) return;
  const qtyEl = row.querySelector('.qty');
  const current = parseInt(qtyEl.textContent, 10);
  const next = current + delta;
  postJSON('/cart/update/', {product_id: productId, quantity: next})
    .then(() => location.reload());
}

function removeFromCart(productId){
  postJSON('/cart/remove/', {product_id: productId})
    .then(() => location.reload());
}

