const authoriseBtn = document.querySelectorAll('.btn_authorise')
const ApprovalSection = document.querySelector('.approve-section')

authoriseBtn.addEventListener('click', () => {
    e.preventDefault();
    ApprovalSection.style.display = 'flex'
})