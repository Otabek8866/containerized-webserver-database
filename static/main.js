//Populating the table with all the entries from database
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
        button.innerHTML = "<button class='favorite styled' type='button' id='" + item.email + "' onClick='delete_entry(this.id)'>Delete</button>";
    });
}

// refresshing the table
function refresh_table() {
    var Table = document.getElementById("table_body");
    Table.innerHTML = "";
    // var Parent = document.getElementById("table_body");
    // while (Parent.hasChildNodes()) {
    //     Parent.removeChild(Parent.firstChild);
    // }
    loadTableData();
}

// opening and closing the form section
function open_form() {
    var submitDiv = document.getElementById("addDiv");
    if (submitDiv.style.display !== "none") {
        submitDiv.style.display = "none";
    } else {
        submitDiv.style.display = "block";
    }
}

// general function to send data to server
// async function send_request(url = '', data = {}, req_type = 'GET') {
//     let answer = await fetch(url, {
//         method: req_type,
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(data)
//     });
//     var status = answer.status
//     return status;
// }

// adding a new entry into database
async function add_new_entry() {
    // check if fields are not empty
    if (check_fields() == false) {
        return;
    }
    // creating json object for new entry
    var jsonData = {};
    var list_items = ['fname', 'lname', 'email', 'phone'];
    list_items.forEach(item => {
        jsonData[item] = document.getElementById(item).value;
    });
    // sending the new entry to server
    let answer = await fetch('add_entry', {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(jsonData)
    });
    //clear fields and show the result
    open_form();
    clear_fields();
    refresh_table();
    // if (answer.status == 200) {
    //     alert("The new contact added successfully. Please refresh the table!")
    // } else {
    //     alert("Problem occured. Please try again!")
    // }
    console.log(answer.status);
}

// clear input fields
function clear_fields() {
    var list_items = ['fname', 'lname', 'email', 'phone'];
    list_items.forEach(item => {
        document.getElementById(item).value = '';
    });
}

// Checking if fields are empty
function check_fields() {
    var list_items = ['fname', 'lname', 'email', 'phone'];
    var status = [];
    list_items.forEach(item => {
        if (document.getElementById(item).value == '') {
            status.push(false)
        } else {
            status.push(true)
        }
    });
    if (status[0] && status[1] && status[2] && status[3]) {
        return;
    } else {
        alert("Please fill the empty places");
        return false;
    }
}
// Deleting the entry with ID
async function delete_entry(email) {
    var jsonData = { 'email': email };

    // sending the new entry to server
    let answer = await fetch('delete', {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(jsonData)
    });
    // refresh the table
    refresh_table();
    console.log(answer.status);
}

loadTableData();