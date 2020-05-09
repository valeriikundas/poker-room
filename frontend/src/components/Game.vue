<template>
  <div>
    <router-link to="/">lobby</router-link>

    <h4>logged in as {{ username }}. table id = {{ table_id }}</h4>
    <br />

    <p>{{pot}}</p>

    <div v-for="i in 5" :key="i" style="display:inline-flex">
      <div>
        <img :src="faceDownCardUrl" class="mr-auto" width="60" />
        <div>AhAd</div>
      </div>
    </div>

    <div>
      <div
        v-for="player in players"
        v-bind:key="player.username"
        v-bind:id="player.username"
        class="w-5"
        style="display: inline-flex"
      >
        <div class="card container">
          <div
            v-if="player.username == username"
            class="card-title bg-warning"
          >{{ player.username }}</div>
          <div v-else class="card-title">{{ player.username }}</div>
          <div class="card-subtitle">{{ player.stack_size }}</div>
          <div class="mx-auto" style="display:inline-flex">
            <img :src="faceDownCardUrl" width="60" />
            <img :src="faceDownCardUrl" width="60" />
          </div>
          <div>AhAd</div>
          <div>{{ player.position }}</div>
        </div>
      </div>
    </div>
    <br />

    <b-input-group>
      <b-button class="bg-danger mr-auto" @click="onFoldAction()">Fold</b-button>
      <b-button class="bg-muted mr-auto" @click="onCheckAction()">Check</b-button>
      <b-button class="bg-primary mr-auto" @click="onCallAction()">Call {{ callSize }}</b-button>
      <b-button class="bg-success mr-auto" @click="onRaiseAction()">Raise {{ raiseSize }}</b-button>
      <b-col class="mr-auto" sm="4">
        <b-form-input
          type="range"
          v-model="raiseSize"
          v-bind:min="minRaiseSize"
          v-bind:max="maxRaiseSize"
        ></b-form-input>
      </b-col>
      <div class="mt-2 mr-auto">raise size: {{ raiseSize }}</div>
    </b-input-group>
  </div>
</template>

<script>
import axios from "../main.js";

export default {
  data() {
    return {
      faceDownCardUrl:
        "https://ic.pics.livejournal.com/dailyafirmation/691132/529371/529371_original.jpg",
      callSize: 0,
      minRaiseSize: 100,
      maxRaiseSize: 200,
      raiseSize: -1,
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
  methods: {
    onHandInit() {
      // TODO:
      this.blinds.small = 0;
      this.blinds.big = 0;
      this.blinds.ante = 0;
      this.pot = 0;
    },
    onRequstAction() {
      // TODO:
      this.callSize = 0;
      this.minRaiseSize = 0;
      this.maxRaiseSize = 0;
      this.raiseSize = this.minRaiseSize;
    },
    onFoldAction() {
      // eslint-disable-next-line
      console.log("fold");
    },
    onCheckAction() {
      // eslint-disable-next-line
      console.log("check");
    },
    onCallAction() {
      // eslint-disable-next-line
      console.log("call", this.callSize);
    },
    onRaiseAction() {
      // eslint-disable-next-line
      console.log("raise", this.raiseSize);
    }
  },
  mounted() {
    this.username = localStorage.getItem("username");
    this.table_id = localStorage.getItem("table_id");

    const path = `http://localhost:5000/tables/${this.table_id}/`;
    axios.get(path).then(res => {
      this.players = res.data["players"];
    });

    // onHandInit();
  }
};
</script>

<style>
</style>