export async function getPlanets() {
    const response = await fetch('http://localhost:5000/api/planets');
    return await response.json();
  }
  