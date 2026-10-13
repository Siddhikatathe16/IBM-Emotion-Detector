
function RunSentimentAnalysis() {
    const textToAnalyze =
        document.getElementById("textToAnalyze").value.trim();

    const systemResponse =
        document.getElementById("system_response");

    if (!textToAnalyze) {
        systemResponse.textContent = "Please enter some text to analyze.";
        return;
    }

    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                systemResponse.textContent = this.responseText;
            } else {
                systemResponse.textContent =
                    this.responseText ||
                    "Emotion detection failed. Please try again.";
            }
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" +
            encodeURIComponent(textToAnalyze),
        true
    );

    xhttp.send();
}
