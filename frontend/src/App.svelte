<script>
	import { onMount } from 'svelte';
	import { getPlanets } from './api';
	import Planet from './Planet.svelte';
  
	let planets = [];
	let filteredPlanets = [];
	let searchTerm = '';
	let isLoading = true;
  
	onMount(async () => {
	  planets = await getPlanets();
	  filteredPlanets = [...planets];
	  isLoading = false;
	});
  
	function filterPlanets() {
	  filteredPlanets = planets.filter(planet => planet.name.toLowerCase().includes(searchTerm.toLowerCase()));
	}
  </script>
  
  <main>
	<div class="search-container">
	  <input type="text" bind:value={searchTerm} on:input={filterPlanets} placeholder="Search by planet name" />
	</div>
  
	{#if isLoading}
	  <p>Loading...</p>
	{:else}
	  <div class="planet-row">
		{#each filteredPlanets as planet (planet.name)}
		  <div class="planet">
			<Planet {planet} />
		  </div>
		{/each}
	  </div>
	{/if}
  </main>
  
  <style>
	main {
	  display: flex;
	  flex-direction: column;
	  align-items: center;
	  overflow: hidden;
	}
  
	.planet-row {
	  display: flex;
	  flex-wrap: wrap;
	  justify-content: center;
	  margin: -10px;
	}
  
	.planet {
	  padding: 10px;
	}
  
	.search-container {
	  text-align: center;
	  margin-bottom: 20px;
	}
  
	.search-container input {
	  padding: 8px;
	  width: 100%;
	  max-width: 300px;
	}
  </style>
  