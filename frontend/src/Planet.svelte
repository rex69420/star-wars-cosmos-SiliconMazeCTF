<!-- src/Planet.svelte -->

<script>
  export let planet;

  // Function to capitalize the first letter of a string
  function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }

  // Function to format numbers with commas
  function formatNumberWithCommas(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }
</script>

<div class="planet">
  <h2>{capitalize(planet.name)}</h2>
  <div class="planet-details">
    <p><strong>Climate:</strong> {capitalize(planet.climate)}</p>
    <p><strong>Population:</strong> {formatNumberWithCommas(planet.population)}</p>
    <p><strong>Terrain:</strong> {capitalize(planet.terrain)}</p>
    <p><strong>Diameter:</strong> {formatNumberWithCommas(planet.diameter)} km</p>
    <p><strong>Gravity:</strong> {planet.gravity}</p>
    <p><strong>Surface Water:</strong> {planet.surface_water}%</p>
    <p><strong>Rotation Period:</strong> {planet.rotation_period} hours</p>
    <p><strong>Orbital Period:</strong> {formatNumberWithCommas(planet.orbital_period)} days</p>
  </div>
</div>

<style>
  .planet {
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 20px;
    margin: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
  }

  .planet h2 {
    margin-top: 0;
  }

  .planet-details {
    margin-top: 10px;
  }

  .planet p {
    margin: 5px 0;
  }
</style>
