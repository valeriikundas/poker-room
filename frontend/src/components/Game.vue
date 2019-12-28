<template>
  <div>
    <router-link to="/">lobby</router-link>

    <h4>logged in as {{ username }}. table id = {{ table_id }}</h4>
    <br />

    <p>{{pot}}</p>

    <div>
      <div v-for="player in players" v-bind:key="player.username" style="display: inline-flex">
        <div class="card container">
          <div class="card-title">{{ player.username }}</div>
          <div class="card-subtitle">{{ player.chip_count }}</div>
          <div>here should be text cards</div>
          <div class="mx-auto" style="display:inline-flex; background-color:yellow;">
            <img
              src="https://previews.123rf.com/images/pandawild/pandawild1509/pandawild150900010/44636299-poker-playing-card-ace-heart.jpg"
              width="60"
            />
            <img
              src="https://previews.123rf.com/images/pandawild/pandawild1509/pandawild150900010/44636299-poker-playing-card-ace-heart.jpg"
              width="60"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      username: "",
      table_id: "",
      players: [],
      pot: 0,
      blinds: {
        small: 0,
        big: 0,
        ante: 0
      }
    };
  },
  mounted() {
    this.username = localStorage.getItem("username");
    this.table_id = localStorage.getItem("table_id");

    const path = `http://localhost:5000/table/${this.table_id}`;
    Axios.get(path).then(res => {
      this.players = res.data["players"];
    });
  }
};
</script>

<style>
</style>