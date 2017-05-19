/* Call getGuides() */
$(document).ready(function() {
  getGuides();
});

/* DEFAULT VALUES */
var page_number = 1;
var result_num_displayed = 10;


/* SEARCH AND FILTER */
$("#search").keypress(function(e) {
    if(e.which == 13) {
      // reset page number to avoid errors
      page_number = 1;
      getGuides();
    }
});

$("#search-button").click(function(){
  // reset page number to avoid errors
  page_number = 1;
  getGuides();
});

$("#filters").change(function(){
  // get the new result number displayed 
  result_num_displayed = $("#result-num-displayed").val();

  // reset page number to avoid errors  
  page_number = 1;

  getGuides();
});
/* END OF SEARCH AND FILTERS */

/* START OF PAGINATION */
$( "#previous" ).click(function() {
  if (page_number > 1) {
    page_number -= 1;
    getGuides();
  }
});

$( "#next" ).click(function() {
  if (page_number < Math.ceil(parseInt($('#total-result-num').html())/result_num_displayed)) {
    page_number += 1;
    getGuides();          
  }
});

$("#pagination").click(function(e){
  // prevents click event if already active
  if($(e.target.parentNode).hasClass('active')){
     return false;
  }           
  // turn string to int for calculation             
  page_number = parseInt(e.target.text);
  getGuides();
})
/* END OF PAGINATION */


/* GET GUIDE FUNCTION */
function getGuides() {

  // Variables

  var search = $("#search").val();
  
  var category = $("#category").val();


  category = "category=" + category + "&";

  $.ajax({
      url: '/api/guide/?' + category,
      data: {
        search: search,
        format: 'json',
        page: page_number,
        page_size: result_num_displayed
      },
      success: function(data, page) {
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

        // Display pagination numbers
        var total_page = Math.ceil(data.count/result_num_displayed);

        var pagination = "";

        for (var k = 1; k <= total_page; k++) {
          pagination +=  "<li " + getActivePage(k) + "><a href='#'>" + k + "</a></li>";
        }

        function getActivePage(number) {
          if (number == page_number) {
            return "class='active'";
          }
          else {
            return "";
          }
        }

        $("#pagination").html(pagination);
        $("#total-result-num").text(data.count);
        $("#guides").html(html_result);
        $(window).trigger('resize');
      }
    });
}

