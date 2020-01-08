<template>
  <div>
    <p>{{error}}</p>
    <router-link v-if="joinedTable" to="/game">game</router-link>

    <div v-if="loggedIn">
      logged in as {{ username }}
      <button class="btn btn-dark" @click="onLogout()">logout</button>
    </div>
    <div v-else>
      <input type="text" v-model="username" />
      <button class="btn btn-dark" @click="onLogin(username)">login</button>
    </div>
    <br />

    <table v-if="tables.length" class="table">
      <thead>
        <tr>
          <th scope="col">table id</th>
          <th scope="col">players count</th>
          <th scope="col">join link</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="table in tables" :key="table.table_id">
          <td>{{ table.table_id }}</td>
          <td>{{ table.players_count }}</td>
          <td>
            <button class="btn btn-dark" @click="onJoin(table)">join</button>
          </td>
        </tr>
      </tbody>
    </table>
    <h1 v-else>no tables</h1>
  </div>
</template>

<script>
import router from "../router";
import axios from "../main.js";

export default {
  data() {
    return {
      error: "",
      tables: [],
      username: "",
      table_id: "",
      loggedIn: false,
      joinedTable: false
    };
  },
  methods: {
    getTables() {
      const path = "tables/";
      axios
        .get(path)
        .then(response => {
          this.tables = response.data["tables"];
        })
        .catch(error =>
          // eslint-disable-next-line
          console.error(error)
        );
    },
    onLogin() {
      const path = "login/";
      axios
        .post(path, { username: this.username })
        .then(() => {
          this.loggedIn = true;

          localStorage.setItem("username", this.username);
          localStorage.setItem("loggedIn", this.loggedIn);
        })
        .catch(error =>
          // eslint-disable-next-line
          console.error(error)
        );
    },
    onLogout() {
      const path = "logout/";
      axios
        .get(path)
        .then(() => {
          this.username = "";
          this.loggedIn = false;
          localStorage.setItem("username", "");
          localStorage.setItem("loggedIn", false);
          router.push({ path: "/" });
        })
        .catch(error =>
          // eslint-disable-next-line
          console.error(error)
        );
    },
    onJoin(table) {
      // FIXME: requests are sent one by one. not in session, without cookies
      let table_id = table.table_id;
      const path = `tables/${this.username}/join/${table_id}/`;
      axios
        .get(path)
        .then(res => {
          if (res.data.status == "error") {
            this.error = res.data;
            return;
          }

          this.joinedTable = true;
          localStorage.setItem("table_id", table_id);
          localStorage.setItem("joinedTable", true);
          router.push({ path: "/game", params: { table_id: table_id } });
        })
        .catch(error =>
          // eslint-disable-next-line
          console.error(error)
        );
    }
  },
  created() {
    this.getTables();

    this.username = localStorage.getItem("username");
    this.loggedIn = Boolean(localStorage.getItem("loggedIn"));

    this.table_id = localStorage.getItem("table_id");
    this.joinedTable = Boolean(localStorage.getItem("joinedTable"));
  },
  mounted() {
    // for manipulating DOM
  }
};
</script>