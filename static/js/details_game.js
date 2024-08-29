function dlc() {
    document.getElementById('dlc').style.display = ''
    document.getElementById('desc').style.display = 'none'
    document.getElementById('requirements').style.display = 'none'
    document.getElementById('lenguages').style.display = 'none'


}
function description() {
    document.getElementById('dlc').style.display = 'none'
    document.getElementById('desc').style.display = ''
    document.getElementById('requirements').style.display = 'none'
    document.getElementById('lenguages').style.display = 'none'


}
function requirements() {
    document.getElementById('dlc').style.display = 'none'
    document.getElementById('desc').style.display = 'none'
    document.getElementById('requirements').style.display = ''
    document.getElementById('lenguages').style.display = 'none'

}

function lenguage() {
    document.getElementById('dlc').style.display = 'none'
    document.getElementById('desc').style.display = 'none'
    document.getElementById('requirements').style.display = 'none'
    document.getElementById('lenguages').style.display = ''
}



/* requirements */
function pc() {
    document.getElementById('pc').style.display = ''
    document.getElementById('mac').style.display = 'none'
    document.getElementById('linux').style.display = 'none'
}
function mac() {
    document.getElementById('pc').style.display = 'none'
    document.getElementById('mac').style.display = ''
    document.getElementById('linux').style.display = 'none'
}

function linux() {
    document.getElementById('pc').style.display = 'none'
    document.getElementById('mac').style.display = 'none'
    document.getElementById('linux').style.display = ''
}