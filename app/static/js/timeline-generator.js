function generateLegend(earliestTime, latestTime) {
  var blocknum = (latestTime - earliestTime) + 1;
  var hourMarkerWidth = 100 / blocknum;

  var markersToAdd = "";

  for (i = earliestTime; i < latestTime; i++) {
    markersToAdd += "<div class='hour-marker'>" + i + "<div class='half-hour-marker'></div></div>";
  }

  markersToAdd += "<div class='hour-marker'>" + latestTime + "</div>";

  $('#timeline-legend').append(markersToAdd);

  $('.hour-marker').css('width', hourMarkerWidth + "%");
}

function addPeriodToTimeline(museumID, earliestTime, latestTime, openTime, closedTime) {
  earliestTime -= 0.5;
  latestTime += 0.5;
  var totalWidth = (latestTime * 60) - (earliestTime * 60);
  var widthOfBlock = (closedTime - openTime)/totalWidth;
  var startOfBlock = (openTime - (earliestTime * 60))/totalWidth;

  $('#museum-' + museumID + ' .museum-open-time').append('<div class="progress-bar open" style="width:' + widthOfBlock * 100 +'%; left:' + startOfBlock * 100 + '%;"></div>');
}
