// Efeito de digitação no título
function initTypeWriter() {
    const heroTitle = document.querySelector('.hero h1');
    if (heroTitle) {
        const originalTitle = heroTitle.textContent;
        heroTitle.textContent = '';
        
        let i = 0;
        function typeWriter() {
            if (i < originalTitle.length) {
                heroTitle.textContent += originalTitle.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            }
        }
        setTimeout(typeWriter, 500);
    }
}

// Inicializar quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    initTypeWriter();
    
    // Adicionar animação aos cards
    const cards = document.querySelectorAll('.feature-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            card.style.transition = 'all 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 300 + (index * 200));
    });
});