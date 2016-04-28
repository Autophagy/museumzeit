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
