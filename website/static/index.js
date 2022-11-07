const deleteNote = (id) => {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({id})
  }).then(() => window.location.href = "/")
}