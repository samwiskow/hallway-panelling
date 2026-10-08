document.querySelectorAll('.gallery').forEach(gallery => {
  const links = [...gallery.querySelectorAll('.gallery-nav a')];
  const figures = [...gallery.querySelectorAll('figure')];
  const show = id => {
    figures.forEach(figure => { figure.hidden = figure.id !== id; });
    links.forEach(link => {
      if (link.hash === '#' + id) link.setAttribute('aria-current', 'true');
      else link.removeAttribute('aria-current');
    });
  };
  show(figures.some(figure => '#' + figure.id === location.hash) ? location.hash.slice(1) : figures[0].id);
  links.forEach(link => link.addEventListener('click', event => {
    event.preventDefault();
    show(link.hash.slice(1));
  }));
});
