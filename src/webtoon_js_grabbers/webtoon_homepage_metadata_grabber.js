// Retrieves all the metadata from the homepage of webtoons
// Reference URL: https://www.webtoons.com/en/originals?weekday=WEDNESDAY&sortOrder=READ_COUNT&webtoonCompleteType=ONGOING


var divElements = [];
for (var i = 2; i <= 8; i++) {
    var xpath = '//*[@id="dailyList"]/div[' + i + ']';
    var divElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (divElement) {
        divElements.push(divElement);
    }
}

var completedSeriesXPath = '//*[@id="content"]/div[2]/div[2]/div';
var completedSeriesDivElement = document.evaluate(completedSeriesXPath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
divElements.push(completedSeriesDivElement);

// Extract information from each li within each ul within each div element
var entries = [];
entries.push('title|author|likes|url'); // Add the header as the first entry
divElements.forEach(function(divElement) {
    var ulElement = divElement.querySelector('ul');
    if (ulElement) {
        var liElements = ulElement.querySelectorAll('li');
        liElements.forEach(function(liElement) {
            var subjElement = liElement.querySelector('p.subj');
            var title = subjElement ? subjElement.textContent.trim() : '';

            var authorElement = liElement.querySelector('p.author');
            var author = authorElement ? authorElement.textContent.trim().replace(/ \/ /g, ',') : '';

            var likesElement = liElement.querySelector('em.grade_num');
            var likes = likesElement ? parseLikes(likesElement.textContent.trim()) : '';

            var urlElement = liElement.querySelector('a.daily_card_item');
            var url = urlElement ? urlElement.getAttribute('href') : '';

            // Add entry to the array
            entries.push(title + '|' + author + '|' + likes + '|' + url);
        });
    }
});

// Log the entire output as a single string
console.log(entries.join('\n'));

// Function to parse likes in the format "67,505" or "58.7M" to integers
function parseLikes(likes) {
    if (likes.includes('M')) {
        return parseInt(parseFloat(likes) * 1000000);
    } else {
        return parseInt(likes.replace(/,/g, ''));
    }
}
