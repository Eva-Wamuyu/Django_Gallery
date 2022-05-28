function copy(anId){
  var copyText = document.getElementById(anId)
  copyText.select()
  document.execCommand('copy')

}
