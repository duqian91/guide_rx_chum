// Call getGuides()
$(document).ready(function() {
  getGuides();
});

// Now changed to press enter or click on search button
$("#search").keypress(function(e) {
    if(e.which == 13) {
        getGuides();
    }
});

$("#search-button").click(getGuides);

$("#filters").change(getGuides);


function getGuides() {

  // Variables
  var result_num_displayed = $("#result-num-displayed").val();

  var search = $("#search").val();
  
  var category = $("#category").val();

  category = "category=" + category + "&";

  $.ajax({
      url: '/api/guide/?' + category,
      data: {
        search: search,
        format: 'json',
        limit: result_num_displayed,     
      },
      success: function(data) {
        var filter_result = data.results;
        var html_result = "";
          for (var i = 0; i < filter_result.length; i++) {
            html_result += "" +
            "<article class='media'>" +
              "<div class='media-left media-middle'>" + 
                "<a target='_blank' href='" + filter_result[i].document_url + "'>" +
                  "<img class='media-object' src='" + filter_result[i].category_img_url + "' >" +
                "</a>" +
              "</div>" +
              "<div class='media-body'>" +
                "<h4 class='media-heading'><a target='_blank' href='" + filter_result[i].document_url + "'>" + filter_result[i].guide_name + "</a></h4>" +
                filter_result[i].description +
                "<div class='tags'>" +
                  displayTags() +
                "</div>" +
              "</div>" +
            "</article>";
          }

        function displayTags() {
          var tag_html = "";
          for (var j = 0; j < filter_result[i].tag.length; j++) {
            tag_html += "" +
            "<span class='label " + filter_result[i].tag[j].color_class + "'>" + filter_result[i].tag[j].tag + "</span> ";
          }
          return tag_html;
        }

        // if (filter_result == "") {
        //   pass;
        // }

        $("#total-result-num").text(data.count);
        $("#guides").html(html_result);
        $(window).trigger('resize');
      }
    });
}
