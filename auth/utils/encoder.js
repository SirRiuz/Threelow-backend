





const payloads = "qwertyuiopasdfghjklñzxcvbnm 0123456789.QWERTYUIOPZXCVBNMLKJHGFDSA-".split("")
const key = "01m2n3b4v5c6x7z8a9sdf.ghjklñpoiuytr ewqASDFGHJKLÑPOIUYTREWQMNBV-CXZ".split("")



function encode(text) {
    var encodeText = ''
    var textArray = text.split("").reverse()

    textArray.map((i) => {
        encodeText += key[payloads.indexOf(i)]
    })
    console.log(encodeText)
    return encodeText
}


encode("Mi nombre es Camila")

