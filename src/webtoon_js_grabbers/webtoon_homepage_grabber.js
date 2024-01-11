// Retrieves all entries from the ONGOING section of webtoons
// Reference URL: https://www.webtoons.com/en/originals?weekday=WEDNESDAY&sortOrder=READ_COUNT&webtoonCompleteType=ONGOING

var divElements = [];
for (var i = 2; i <= 8; i++) {
    var xpath = '//*[@id="dailyList"]/div[' + i + ']';
    var divElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (divElement) {
        divElements.push(divElement);
    }
}

var entries = [];
divElements.forEach(function(divElement) {
    var ulElement = divElement.querySelector('ul');
    if (ulElement) {
        var liElements = ulElement.querySelectorAll('li');
        liElements.forEach(function(liElement) {
            var subjElement = liElement.querySelector('p.subj');
            var subject = subjElement ? subjElement.textContent.trim() : '';

            var urlElement = liElement.querySelector('a.daily_card_item');
            var url = urlElement ? urlElement.getAttribute('href') : '';

            entries.push(subject + '|' + url);
        });
    }
});

console.log(entries.join('\n'));
