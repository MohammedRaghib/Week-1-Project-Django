const handleview = (shown) => {
    const form = document.querySelector('.add-form');
    const addbtn = document.getElementById('addbtn');
    if (shown) {
        form.style.display = 'block';
        addbtn.style.display = 'none';
        const editform = document.querySelector('.edit-form');
        editform.style.display = 'none';
    } else {
        form.style.display = 'none';
        addbtn.style.display = 'block';
    }
};
const editfood = (fid, fname, fcal) => {
    const Name = document.getElementById('edit-name-input');
    const Calorie = document.getElementById('edit-calorie-input');
    const save = document.getElementById('save');
    save.value = fid
    Name.value = fname;
    Calorie.value = fcal;
    const editform = document.querySelector('.edit-form');
    editform.style.display = 'block';
}

const close = () => {
    const editform = document.querySelector('.edit-form');
    editform.style.display = 'none';
}

const reassure = (event) => {
    event.preventDefault();
    let accept = confirm('Are you sure you want to delete everything?')

    if (accept) {
        document.getElementById('delete-everything').submit();
    }
}
