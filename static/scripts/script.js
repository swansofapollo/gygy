function change_language(language) {
    $.post("/change_language", {
        data: JSON.stringify(language)
    })
    window.location.href = "/";
}

THEME = 'light'

$(document).ready(function() {
    $.get({
        url: "/theme",
        success: function(theme) {
            console.log(theme + '?')
            THEME = theme
            set_theme(theme) 
        }
    })
})

$('body').bind('beforeunload',function(){
    $.post("/theme", {
        data: JSON.stringify(THEME)
    })
    console.log(THEME)
})

function set_theme(theme) {
    if (theme == 'dark') {
        $("nav").removeClass('navbar-light bg-light')
        $("nav").addClass('navbar-dark bg-dark')
        $("body").addClass('body-dark')
        $("footer").addClass('footer-dark')
        $("div").addClass(function (index, current_class) {
            var added_class
            if (current_class == 'card') {
                added_class = 'card-dark'
            }
            if (current_class == 'card-body') {
                added_class = 'card-body-dark'
            }
            return added_class
        })
    } else if (theme == 'light') {
        $("nav").removeClass('navbar-dark bg-dark')
        $("nav").addClass('navbar-light bg-light')
        $("body").removeClass('body-dark')
        $("footer").removeClass('footer-dark')
        $("div").removeClass('card-body-dark card-dark')
    }
    $.post("/theme", {
        data: JSON.stringify(THEME)
    })
    console.log(THEME)
}

function switch_theme() {
    if (THEME == 'light') {
        $("nav").removeClass('navbar-light bg-light')
        $("nav").addClass('navbar-dark bg-dark')
        $("body").addClass('body-dark')
        $("footer").addClass('footer-dark')
        $("div").addClass(function (index, current_class) {
            var added_class
            if (current_class == 'card') {
                added_class = 'card-dark'
            }
            if (current_class == 'card-body') {
                added_class = 'card-body-dark'
            }
            return added_class
        })
        THEME = 'dark'
    } else if (THEME == 'dark') {
        $("nav").removeClass('navbar-dark bg-dark')
        $("nav").addClass('navbar-light bg-light')
        $("body").removeClass('body-dark')
        $("footer").removeClass('footer-dark')
        $("div").removeClass('card-body-dark card-dark')
        THEME = 'light'
    }
    $.post("/theme", {
        data: JSON.stringify(THEME)
    })
    console.log(THEME)
}

