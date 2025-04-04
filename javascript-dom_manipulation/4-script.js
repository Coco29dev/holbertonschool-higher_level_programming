document.getElementById('add_item').addEventListener('click', function () {
  const my_list = document.querySelector('ul.my_list');
  const li = document.createElement('li');
  li.textContent = 'Item';
  my_list.appendChild(li);
})
