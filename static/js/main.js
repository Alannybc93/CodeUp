// ===== CODEUP MAIN JAVASCRIPT =====

document.addEventListener('DOMContentLoaded', function() {
    console.log('CodeUp JS carregado!');
    
    // ===== INICIALIZAÇÃO =====
    initTooltips();
    initProgressBars();
    initNotifications();
    initDarkModeToggle();
    initMobileMenu();
    initCodeEditor();
    initGamification();
    
    // ===== FUNÇÕES DE INICIALIZAÇÃO =====
    
    function initTooltips() {
        // Inicializar tooltips do Bootstrap
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
    
    function initProgressBars() {
        // Animar barras de progresso quando visíveis
        const progressBars = document.querySelectorAll('.progress-bar');
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const progressBar = entry.target;
                    const width = progressBar.getAttribute('aria-valuenow') || '0';
                    progressBar.style.width = width + '%';
                    observer.unobserve(progressBar);
                }
            });
        }, { threshold: 0.5 });
        
        progressBars.forEach(bar => observer.observe(bar));
    }
    
    function initNotifications() {
        // Auto-fechar alerts após 5 segundos
        const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
        alerts.forEach(alert => {
            setTimeout(() => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 5000);
        });
    }
    
    function initDarkModeToggle() {
        const darkModeToggle = document.getElementById('darkModeToggle');
        if (darkModeToggle) {
            darkModeToggle.addEventListener('click', function() {
                document.body.classList.toggle('dark-mode');
                localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
                
                // Atualizar ícone
                const icon = this.querySelector('i');
                if (document.body.classList.contains('dark-mode')) {
                    icon.classList.remove('fa-moon');
                    icon.classList.add('fa-sun');
                } else {
                    icon.classList.remove('fa-sun');
                    icon.classList.add('fa-moon');
                }
            });
            
            // Carregar preferência salva
            if (localStorage.getItem('darkMode') === 'true') {
                document.body.classList.add('dark-mode');
                const icon = darkModeToggle.querySelector('i');
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            }
        }
    }
    
    function initMobileMenu() {
        const mobileMenuToggle = document.querySelector('.navbar-toggler');
        if (mobileMenuToggle) {
            mobileMenuToggle.addEventListener('click', function() {
                document.body.classList.toggle('menu-open');
            });
        }
    }
    
    function initCodeEditor() {
        // Inicializar editores de código se existirem
        const codeEditors = document.querySelectorAll('.code-editor');
        if (codeEditors.length > 0 && typeof CodeMirror !== 'undefined') {
            codeEditors.forEach(editor => {
                const language = editor.getAttribute('data-language') || 'python';
                CodeMirror.fromTextArea(editor, {
                    lineNumbers: true,
                    mode: language,
                    theme: 'material',
                    indentUnit: 4,
                    lineWrapping: true
                });
            });
        }
    }
    
    function initGamification() {
        // Efeitos de gamificação
        const xpElements = document.querySelectorAll('.xp-gain');
        xpElements.forEach(element => {
            element.addEventListener('click', function() {
                this.classList.add('pulse');
                setTimeout(() => this.classList.remove('pulse'), 1000);
            });
        });
    }
    
    // ===== FUNÇÕES DE UTILIDADE =====
    
    window.CodeUp = {
        // Mostrar notificação
        showNotification: function(message, type = 'success') {
            const notification = document.createElement('div');
            notification.className = `alert alert-${type} alert-dismissible fade show`;
            notification.innerHTML = `
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            `;
            
            const container = document.querySelector('.notification-container') || document.body;
            container.prepend(notification);
            
            setTimeout(() => {
                const bsAlert = new bootstrap.Alert(notification);
                bsAlert.close();
            }, 5000);
        },
        
        // Formatar número com pontos
        formatNumber: function(num) {
            return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        },
        
        // Calcular tempo restante
        calculateTimeRemaining: function(endDate) {
            const now = new Date();
            const end = new Date(endDate);
            const diff = end - now;
            
            if (diff <= 0) return 'Expirado';
            
            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            
            return `${days}d ${hours}h ${minutes}m`;
        },
        
        // Copiar para área de transferência
        copyToClipboard: function(text) {
            navigator.clipboard.writeText(text)
                .then(() => this.showNotification('Copiado para área de transferência!', 'success'))
                .catch(() => this.showNotification('Erro ao copiar', 'danger'));
        },
        
        // Validar formulário
        validateForm: function(formId) {
            const form = document.getElementById(formId);
            if (!form) return false;
            
            let isValid = true;
            const inputs = form.querySelectorAll('[required]');
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.classList.add('is-invalid');
                    isValid = false;
                } else {
                    input.classList.remove('is-invalid');
                }
            });
            
            return isValid;
        },
        
        // Carregar mais conteúdo (infinite scroll)
        loadMoreContent: function(url, containerId, page = 1) {
            return fetch(`${url}?page=${page}`)
                .then(response => response.json())
                .then(data => {
                    const container = document.getElementById(containerId);
                    if (container && data.html) {
                        container.innerHTML += data.html;
                        return data.has_more;
                    }
                    return false;
                })
                .catch(error => {
                    console.error('Erro ao carregar conteúdo:', error);
                    return false;
                });
        },
        
        // Atualizar contador em tempo real
        startLiveCounter: function(elementId, targetValue, duration = 2000) {
            const element = document.getElementById(elementId);
            if (!element) return;
            
            let startValue = 0;
            const increment = targetValue / (duration / 16); // 60fps
            
            const timer = setInterval(() => {
                startValue += increment;
                if (startValue >= targetValue) {
                    element.textContent = this.formatNumber(Math.round(targetValue));
                    clearInterval(timer);
                } else {
                    element.textContent = this.formatNumber(Math.round(startValue));
                }
            }, 16);
        },
        
        // Iniciar temporizador
        startTimer: function(elementId, seconds) {
            const element = document.getElementById(elementId);
            if (!element) return;
            
            let timeLeft = seconds;
            
            const timer = setInterval(() => {
                const minutes = Math.floor(timeLeft / 60);
                const secs = timeLeft % 60;
                
                element.textContent = `${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
                
                if (timeLeft <= 0) {
                    clearInterval(timer);
                    element.textContent = '00:00';
                    this.showNotification('Tempo esgotado!', 'warning');
                }
                
                timeLeft--;
            }, 1000);
        }
    };
    
    // ===== EVENT LISTENERS GLOBAIS =====
    
    // Smooth scroll para âncoras
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Confirmação para ações perigosas
    document.querySelectorAll('[data-confirm]').forEach(button => {
        button.addEventListener('click', function(e) {
            const message = this.getAttribute('data-confirm') || 'Tem certeza?';
            if (!confirm(message)) {
                e.preventDefault();
                e.stopPropagation();
            }
        });
    });
    
    // Lazy loading para imagens
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => imageObserver.observe(img));
    }
    
    // ===== INICIALIZAR COMPONENTES ESPECÍFICOS =====
    
    // Inicializar gráficos se Chart.js estiver disponível
    if (typeof Chart !== 'undefined') {
        initCharts();
    }
    
    function initCharts() {
        // Gráfico de progresso
        const progressChartEl = document.getElementById('progressChart');
        if (progressChartEl) {
            const ctx = progressChartEl.getContext('2d');
            new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Completo', 'Restante'],
                    datasets: [{
                        data: [75, 25],
                        backgroundColor: ['#4361ee', '#e9ecef'],
                        borderWidth: 0
                    }]
                },
                options: {
                    cutout: '70%',
                    plugins: {
                        legend: { display: false },
                        tooltip: { enabled: false }
                    }
                }
            });
        }
        
        // Gráfico de atividades
        const activityChartEl = document.getElementById('activityChart');
        if (activityChartEl) {
            const ctx = activityChartEl.getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
                    datasets: [{
                        label: 'Exercícios',
                        data: [12, 19, 8, 15, 22, 18, 25],
                        borderColor: '#4361ee',
                        backgroundColor: 'rgba(67, 97, 238, 0.1)',
                        tension: 0.4,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            grid: { color: 'rgba(0,0,0,0.05)' }
                        },
                        x: {
                            grid: { color: 'rgba(0,0,0,0.05)' }
                        }
                    }
                }
            });
        }
    }
});
