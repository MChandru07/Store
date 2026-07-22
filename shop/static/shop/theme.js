(function(){
  const root = document.documentElement;
  const btnLight = document.getElementById('themeBtnLight');
  const btnDark = document.getElementById('themeBtnDark');
  const btnSystem = document.getElementById('themeBtnSystem');

  function getSystemTheme(){
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function setPressed(active){
    const set = (btn, val) => { if(btn) btn.setAttribute('aria-pressed', val ? 'true' : 'false'); };
    set(btnLight, active==='light');
    set(btnDark, active==='dark');
    set(btnSystem, active==='system');
  }

  function applyTheme(mode){
    if(mode==='system'){
      root.setAttribute('data-theme', getSystemTheme());
      setPressed('system');
      return;
    }
    root.setAttribute('data-theme', mode);
    setPressed(mode);
  }

  const saved = localStorage.getItem('theme-mode') || 'system';
  applyTheme(saved);

  function bind(btn, mode){
    if(!btn) return;
    btn.addEventListener('click', () => {
      localStorage.setItem('theme-mode', mode);
      applyTheme(mode);
    });
  }

  bind(btnLight,'light');
  bind(btnDark,'dark');
  bind(btnSystem,'system');

  if(window.matchMedia){
    const mql = window.matchMedia('(prefers-color-scheme: dark)');
    mql.addEventListener('change', () => {
      if(localStorage.getItem('theme-mode')==='system'){
        applyTheme('system');
      }
    });
  }
})();

