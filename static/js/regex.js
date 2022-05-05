const btn = document.getElementById('dropdown-btn');
const btn2 = document.getElementById('dropdown-btn-2');

btn.addEventListener("click", function () {
    document.getElementById("delimiter-dropdown").classList.toggle("show");
});
btn2.addEventListener("click", function () {
    document.getElementById("flags-dropdown").classList.toggle("show");
});

function setDelimiterOne() {
    btn.value = "r " + document.getElementById("one").textContent
}

function setDelimiterTwo() {
    btn.value = "r " + document.getElementById("two").textContent
}

function setDelimiterThree() {
    btn.value = "r " + document.getElementById("three").textContent
}

function setDelimiterThreeDouble() {
    btn.value = "r " + document.getElementById("three-double").textContent
}

window.addEventListener('click', function (e) {

    if (e.target.closest('.input-group-prepend') === null) {
        closeDropdown('#delimiter-dropdown');
    }
    if (e.target.closest('.input-group-append') === null) {
        closeDropdown('#flags-dropdown');
    }
    if (e.target.closest('#delimiter-dropdown') != null) {
        closeDropdown('.dropdown-menu')
    }
});


function setFlag(flagId, char, anotherFlagId= null, anotherChar = null) {
        if (document.getElementById(flagId).checked) {
            if (anotherFlagId != null && document.getElementById(anotherFlagId).checked) {
                document.getElementById(anotherFlagId).checked = false
                btn2.textContent = btn2.textContent.replace(anotherChar, '')
            }
            btn2.textContent = btn2.textContent + char
        } else {
            btn2.textContent = btn2.textContent.replace(char, '')
        }
}

function setTestFlag(flagId, char) {
    btn2.textContent = ''
    document.getElementById('global').checked = false
    document.getElementById('multiline').checked = false
    document.getElementById('insens').checked = false
    document.getElementById('extended').checked = false
    document.getElementById('single-line').checked = false
    document.getElementById('unicode').checked = false
    document.getElementById('ascii').checked = false
    btn2.textContent = char
    document.getElementById(flagId).checked = true
}

function setFunction(flagId, rejectFlagId) {
    document.getElementById(flagId).checked = true
    document.getElementById(rejectFlagId).checked = false
    var element = document.getElementById('subs-container')
    if (flagId == 'substitution') {
        element.style.display = "block"
        element = document.getElementById('test-string')
        element.style.height = "calc(70vh - 200px)"
    } else {
        element.style.display = "none"
        element = document.getElementById('test-string')
        element.style.height = "calc(100vh - 200px)"
    }
}

function closeDropdown(str) {
    console.log('run');

    document.querySelectorAll(str).forEach(function (container) {
        container.classList.remove('show')
    });


}