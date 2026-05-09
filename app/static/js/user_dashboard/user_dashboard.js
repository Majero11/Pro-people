const leaveRequestSection = document.querySelector('.leave-request-section');
const leaveRequestForm = document.querySelector('.leave-request-form');
const leaveApplyBtn = document.querySelector('.apply-btn');
const leaveRequestBtn = document.querySelector('.btn_request_leave');

leaveRequestBtn.addEventListener('click', () => {
    leaveRequestSection.style.display = 'flex';
});
