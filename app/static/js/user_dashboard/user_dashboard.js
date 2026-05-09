const leaveRequestSection = document.querySelector('.leave-request-section');
const leaveRequestForm = document.querySelector('.leave-request-form');
const leaveApplyBtn = document.querySelector('.apply-btn');
const leaveRequestBtn = document.querySelector('.btn_request_leave');
const updateDetailsSection = document.querySelector('.User-details-Update-section');
const updateBtn = document.querySelector('.update-btn');
const updateDetailsBtn = document.querySelector('.btn_update_details');

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

