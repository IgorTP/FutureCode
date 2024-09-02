function onClick(button) {
    var codeBlock = button.parentNode;
    var tempInput = document.createElement("textarea");
    tempInput.value = codeBlock.querySelector("pre code").textContent.trim();

    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);

    var copyNotification = codeBlock.querySelector(".btn_notification");
    copyNotification.classList.add("show");
    setTimeout(() => {
      copyNotification.classList.remove("show");
    }, 1000);
}
