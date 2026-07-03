async function getStatus() {

    const response = await fetch("/api/status");

    return await response.json();

}