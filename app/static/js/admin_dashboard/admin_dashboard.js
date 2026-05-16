const leaveRequestSection = document.querySelector('.leave-request-section');
const leaveRequestForm = document.querySelector('.leave-request-form');
const leaveApplyBtn = document.querySelector('.apply-btn');
const leaveRequestBtn = document.querySelector('.btn_request_leave');
const updateDetailsSection = document.querySelector('.User-details-Update-section');
const updateBtn = document.querySelector('.update-btn');
const updateDetailsBtn = document.querySelector('.btn_update_details');
const tabs = document.querySelector('.tabs');
const Users = document.querySelector('.users');
const Request = document.querySelector('.requests');
const AdminRequest = document.querySelector('.admin_requests');
const reviewRequest = document.querySelector('.activity-section');



leaveRequestBtn.addEventListener('click', () => {
    leaveRequestSection.style.display = 'none';
    updateDetailsSection.style.display = 'flex';
    
    leaveRequestSection.style.display = 'flex';
    updateDetailsSection.style.display = 'none';
});

updateDetailsBtn.addEventListener('click', () => {
    updateDetailsSection.style.display = 'none';
    leaveRequestSection.style.display = 'flex';

    updateDetailsSection.style.display = 'flex';
    leaveRequestSection.style.display = 'none';
});

Users.addEventListener('click', () => {
    Users.style.background = '#037A5D';
    Users.style.color = '#fff';
    Request.style.color = '#037A5D';
    Request.style.background = 'none';
    AdminRequest.style.color = '#037A5D';
    AdminRequest.style.background = 'none';
});

Request.addEventListener('click', () => {
    reviewRequest.style.display = 'flex'
    Request.style.background = '#037A5D';
    Request.style.color = '#fff';
    Users.style.background = 'none';
    Users.style.color = '#037A5D';
    AdminRequest.style.color = '#037A5D';
    AdminRequest.style.background = 'none';
});

AdminRequest.addEventListener('click', () => {
    AdminRequest.style.background = '#037A5D';
    AdminRequest.style.color = '#fff';
    Users.style.background = 'none';
    Users.style.color = '#037A5D';
    Request.style.color = '#037A5D';
    Request.style.background = 'none';
});