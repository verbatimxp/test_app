$('#push-title').keyup(function () {
    const val = $('#push-title').val();
    $('.text-push').html(val);
});

$('#push-name').keyup(function () {
    const val = $('#push-name').val();
    $('.name-push').html(val);
});

// Mozilla display push-images
const image_ios = document.getElementById("image-ios");
const image_android = document.getElementById("image-android");

if (image_ios.getAttribute("src") == '#' || image_android.getAttribute("src") == '#') {
    document.getElementById('image-ios').style.display = 'none';
    document.getElementById('image-android').style.display = 'none';
}
var image_push = document.getElementById('image-push')

function readURL(s) {
    if (image_push.files && image_push.files[0]) {
        const reader = new FileReader();

        reader.onload = function (e) {
            $('.blah').attr('src', e.target.result);
        }

        reader.readAsDataURL(image_push.files[0]);
    }
}

$("#image-push").change(function () {
    document.getElementById('image-ios').style.display = 'block';
    document.getElementById('image-android').style.display = 'block';
    readURL(this);
});
