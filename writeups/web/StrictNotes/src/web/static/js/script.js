const urlParams = new URLSearchParams(window.location.search);

if (urlParams.has('error') && document.getElementById('form')) {
  const errorText = document.createElement('div');
  errorText.id = 'errorText';
  errorText.classList.add('error-text');
  errorText.textContent = urlParams.get('error');

  const noteForm = document.getElementById('form');
  noteForm.appendChild(errorText);
}

if (urlParams.has('message') && document.getElementById('form')) {
  const messageText = document.createElement('div');
  messageText.id = 'messageText';
  messageText.classList.add('message-text');
  messageText.textContent = urlParams.get('message');

  const noteForm = document.getElementById('form');
  noteForm.appendChild(messageText);
} 