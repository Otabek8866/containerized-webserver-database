async function loadTableData() {
    var response = await fetch("contacts");
    var contacts = await response.json();

    const table = document.getElementById("table_body");
    contacts.forEach(item => {
        let row = table.insertRow();
        let id = row.insertCell(0);
        id.innerHTML = item.id;
        let first_name = row.insertCell(1);
        first_name.innerHTML = item.first_name;
        let last_name = row.insertCell(2);
        last_name.innerHTML = item.last_name;
        let email = row.insertCell(3);
        email.innerHTML = item.email;
        let phone = row.insertCell(4);
        phone.innerHTML = item.phone;
        let button = row.insertCell(5);
        button.innerHTML = "<button class='favorite styled' type='button' id='" + item.id + "' onClick='reply_click(this.id)'>Delete</button>";
    });
}

function reply_click(clicked_id) {
    alert(clicked_id);
}

// Updating table
function refresh_table() {
    var Table = document.getElementById("table_body");
    Table.innerHTML = "";
    // var Parent = document.getElementById("table_body");
    // while (Parent.hasChildNodes()) {
    //     Parent.removeChild(Parent.firstChild);
    // }
    loadTableData();
}

loadTableData();