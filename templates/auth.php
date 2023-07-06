<html>
<head>
    <title>Phone Number Authentication with Firebase Web</title>
    <!-- Firebase CDN -->

<!--<script src="https://www.gstatic.com/firebasejs/9.4.0/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.4.0/firebase-firestore.js"></script>-->


</head>

<body>
<h1>Enter number to create account</h1>
<form>
    <input type="text" id="number" placeholder="+94*********">
    <div id="recaptcha-container"></div>
    <button type="button" onclick="phoneAuth();">SendCode</button>
</form><br>
<h1>Enter Verification code</h1>
<form>
    <input type="text" id="verificationCode" placeholder="Enter verification code">
    <button type="button" onclick="codeverify();">Verify code</button>

</form>




<script src="https://www.gstatic.com/firebasejs/6.0.2/firebase.js"></script>
<script>
    // Your web app's Firebase configuration
    var firebaseConfig = {
        apiKey: "AIzaSyDsseqXi1GvuH6M-P2QjlAvpe9KLN1bfUg",
        authDomain: "newauth-c9a4d.firebaseapp.com",
        databaseURL: "https://fir-web-b823f.firebaseio.com",
        projectId: "newauth-c9a4d",
        storageBucket: "newauth-c9a4d.appspot.com",
        messagingSenderId: "254214237623",
        appId: "1:254214237623:web:5ade8301a7470fb6684c32"
    };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
</script>
<script src="numberauth.js" type="text/javascript"></script>
</body>
</html>