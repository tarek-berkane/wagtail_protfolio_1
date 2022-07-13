const menu_close = "header-menu-hidden";
const menu_id_name = "header-menu";

function toggle_menu() {
    var menu = document.getElementById(menu_id_name);
    menu.classList.toggle(menu_close);
}

// SEARCH PAGE
const search_parameters = 'search-parameters'

const CLOSED_FILTER = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-filter stroke-white w-8 h-8 " width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2c3e50" fill="none" stroke-linecap="round" stroke-linejoin="round">
<path stroke="none" d="M0 0h24v24H0z" fill="none"/>
<path d="M5.5 5h13a1 1 0 0 1 .5 1.5l-5 5.5l0 7l-4 -3l0 -4l-5 -5.5a1 1 0 0 1 .5 -1.5" />
</svg>`

const OPENED_FILTER = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-x stroke-white w-8 h-8 " width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2c3e50" fill="none" stroke-linecap="round" stroke-linejoin="round">
<path stroke="none" d="M0 0h24v24H0z" fill="none"/>
<line x1="18" y1="6" x2="6" y2="18" />
<line x1="6" y1="6" x2="18" y2="18" />
</svg>`

function toggle_search_filter_new(elem) {
    var filter_container_elem = document.getElementById(search_parameters);
    if (filter_container_elem) {
        if (filter_container_elem.classList.contains('hidden')) {
            filter_container_elem.classList.remove('hidden')
            elem.innerHTML = OPENED_FILTER;
        } else {
            filter_container_elem.classList.add('hidden')
            elem.innerHTML = CLOSED_FILTER;
        }
    }
}


// PROJECT PAGE
const icon_container_name = "icon-area";
const project_bio_body_name = "project-bio-content";

const open_bio_icon = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-plus w-5 h-5" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2c3e50" fill="none" stroke-linecap="round" stroke-linejoin="round">
<path stroke="none" d="M0 0h24v24H0z" fill="none"/>
<line x1="12" y1="5" x2="12" y2="19" />
<line x1="5" y1="12" x2="19" y2="12" />
</svg>`

const close_bio_icon = `
<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-minus w-5 h-5" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2c3e50" fill="none" stroke-linecap="round" stroke-linejoin="round">
<path stroke="none" d="M0 0h24v24H0z" fill="none"/>
<line x1="5" y1="12" x2="19" y2="12" />
</svg>`


function toggle_bio(elem) {
    var icon_container = elem.getElementsByClassName(icon_container_name)[0];
    var project_body_elem = elem.getElementsByClassName(project_bio_body_name)[0];
    if (project_body_elem && icon_container) {
        if (project_body_elem.classList.contains('hidden')) {
            project_body_elem.classList.remove('hidden')
            icon_container.innerHTML = close_bio_icon;
        } else {
            project_body_elem.classList.add('hidden')
            icon_container.innerHTML = open_bio_icon;

        }
    }
}