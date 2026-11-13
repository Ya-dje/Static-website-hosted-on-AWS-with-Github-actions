/* =============================================
   OLIVE'S SPACE — products.js
   ============================================= */

const filterTabs = document.querySelectorAll('.filter-tab');
const productCards = document.querySelectorAll('#productsGrid .product-card');
const resultsCount = document.getElementById('resultsCount');

filterTabs.forEach(tab => {
  tab.addEventListener('click', () => {
    filterTabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');

    const filter = tab.dataset.filter;
    let visible = 0;

    productCards.forEach(card => {
      const cat = card.dataset.category;
      const show = filter === 'all' || cat === filter;
      card.classList.toggle('hidden', !show);
      if (show) visible++;
    });

    resultsCount.textContent = `${visible} item${visible !== 1 ? 's' : ''}`;
  });
});
