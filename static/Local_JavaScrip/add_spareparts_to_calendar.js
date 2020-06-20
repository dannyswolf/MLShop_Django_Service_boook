function hide() {
  var x = document.getElementById("warehouse");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}


const table = document.getElementById("warehouse");
const my_form = document.getElementById('my-form')


function add_btn(x){
  var item_id = all_items[x].id
  var item_perigrafi = all_items[x].ΠΕΡΙΓΡΑΦΗ
  var item_kodikos = all_items[x].ΚΩΔΙΚΟΣ
  var item_temaxia = 1;
  
  const form = document.querySelector('form');
  const data = Object.fromEntries(new FormData(form).entries());
  var Customer_ID = data.Customer_ID
  var Copier_ID =  data.Copier_ID
  var Service_ID = data.Service_ID
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  console.log(csrftoken)
  const data_to_send = {

    ΠΕΡΙΓΡΑΦΗ: item_perigrafi,
    ΚΩΔΙΚΟΣ: item_kodikos,
    ΜΗΧΑΝΗΜΑ: Copier_ID,
    Service_ID: Service_ID,
    Customer_ID: Customer_ID,
  }
  
  
  const xhr = new XMLHttpRequest() 

  console.log("data_to_send", data_to_send)

  const method = 'GET'
  const url = "../../spareparts/add_spareparts"
  // const responseType = "json"
  // xhr.responseType = responseType
  xhr.open(method, url)
  xhr.setRequestHeader("X-CSRFToken", csrftoken)
  xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
  xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
  xhr.onload = function() {

    console.log(xhr.response, xhr.status)

  }
  xhr.send();
}

var all_items = [];

function load_A_ΟΡΟΦΟΣ() {
    const xhr = new XMLHttpRequest()
    const method = 'GET'
    const url = "../../warehouse/A_ΟΡΟΦΟΣ-json"
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function() {

    const serverResponse = xhr.response

    const head = `<table class="table table-hover table-bordered table-sm" id="data-table">
    <thead>
    <tr class="table-success">
        <th>ΕΤΑΙΡΙΑ</th>
        <th>ΠΕΡΙΓΡΑΦΗ</th>
        <th>ΚΩΔΙΚΟΣ</th>
        <th>ΤΕΜΑΧΙΑ</th>
        <th>ΤΙΜΗ</th>
        <th>ΣΥΝΟΛΟ</th>
        <th>Προσθήκη</th>
    </tr>
    </thead>
    <tbody>`;

    const footer = `</tr>
    </tbody>
      <tfoot>
        <tr class="table-success">
          <th>ΕΤΑΙΡΙΑ</th>
          <th>ΠΕΡΙΓΡΑΦΗ</th>
          <th>ΚΩΔΙΚΟΣ</th>
          <th>TEMAXIA</th>
          <th>ΤΙΜΗ</th>
          <th>ΣΥΝΟΛΟ</th>
          <th>Προσθήκη</th>
        </tr>
      </tfoot>
    </table>`;

    var listed_items = serverResponse.response
    
    var final_item = ""
    var i;
    for (i=0; i<listed_items.length; i++) {
        all_items.push(listed_items[i])
       

        var company_item =  '<tr align="center"> <td><a href="../warehouse/A_ΟΡΟΦΟΣ/'+listed_items[i].id + '">' + listed_items[i].ΕΤΑΙΡΙΑ + '</a> </td>';
        var description_item =  '<td><a href="../warehouse/A_ΟΡΟΦΟΣ/'+listed_items[i].id + '">' + listed_items[i].ΠΕΡΙΓΡΑΦΗ + '</a> </td>';
        var code_item =  '<td><a href="../warehouse/A_ΟΡΟΦΟΣ/'+listed_items[i].id + '">' + listed_items[i].ΚΩΔΙΚΟΣ + '</a> </td>';
        var pieces_item =  '<td><a href="../warehouse/A_ΟΡΟΦΟΣ/'+listed_items[i].id + '">' + listed_items[i].TEMAXIA + '</a> </td>';
        var price_item =  '<td><a href="../warehouse/A_ΟΡΟΦΟΣ/'+listed_items[i].id + '">' + listed_items[i].ΤΙΜΗ + '</a> </td>';
        var total_item =  '<td><a href="../warehouse/A_ΟΡΟΦΟΣ/'+ listed_items[i].id + '">' + listed_items[i].ΣΥΝΟΛΟ + '</a> </td>';

        var notes_item =   "<td><button onclick=add_btn(" + i +") id=" + i + " class='btn btn-primary'>Προσθήκη</button></td></tr>";
        
        final_item +=  company_item + description_item + code_item + pieces_item + price_item + total_item + notes_item                           
      
      }
    var final_table = head + final_item + footer
    table.innerHTML = final_table

   
                         }


xhr.send();
}

load_A_ΟΡΟΦΟΣ(table)



