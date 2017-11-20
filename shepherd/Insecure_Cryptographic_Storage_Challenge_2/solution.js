var input = 'DwsDagmwhziArpmogWaSmmckwhMoEsmgmxlivpDttfjbjdxqBwxbKbCwgwgUyam'
theKey = "kpoisaijdieyjaf";
var theAlphabet =   "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz";

// Validate theKey:
theKey = theKey.toUpperCase();
var theKeysLength = theKey.length;
var i;
var adjustedKey = "";
for(i = 0; i < theKeysLength; i ++)
{
    var currentKeyChar = theAlphabet.indexOf(theKey.charAt(i));
        if(currentKeyChar < 0)
            continue;
        adjustedKey += theAlphabet.charAt(currentKeyChar);
}

theKey = adjustedKey;
theKeysLength = theKey.length;

// Transform input:
var inputLength = input.length;
var output = "";
var theKeysCurrentIndex = 0;
for(i = 0; i < inputLength; i ++)
{
    var currentChar = input.charAt(i);
        var currentCharValue = theAlphabet.indexOf(currentChar);
        if(currentCharValue < 0)
        {
            output += currentChar;
                continue;
        }

    var lowercase = currentCharValue >= 26 ? true : false;
        //currentCharValue += theAlphabet.indexOf(theKey.charAt(theKeysCurrentIndex));
    currentCharValue -= theAlphabet.indexOf(theKey.charAt(theKeysCurrentIndex));

        currentCharValue += 26;
        if(lowercase)
            currentCharValue = currentCharValue % 26 + 26;
        else
            currentCharValue %= 26;
        output += theAlphabet.charAt(currentCharValue);
        theKeysCurrentIndex =(theKeysCurrentIndex + 1) % theKeysLength;
}

console.log('Key=' + output);
