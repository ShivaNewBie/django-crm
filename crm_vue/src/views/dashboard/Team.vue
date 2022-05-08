<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ team.name }}</h1>
                
                <hr>
                <p><strong>Plan: </strong>{{$store.state.team.plan}}</p>
                <p><strong>Max clients: </strong>{{$store.state.team.max_clients}}</p>
                <p><strong>Max leads: </strong>{{$store.state.team.max_leads}}</p>
                <p>
                    <router-link :to="{'name':'Plans'}">
                            Change Plan
                    </router-link>
                </p>
                <hr>
                <router-link :to="{'name':'AddMember'}" class='button is-primary'>Add Member</router-link>
                 <!-- to='/dashboard/team/add-member' above is better so when we change the url in router we dont have to manually change it here also-->
            </div>
            <div class="column is-12">
                <h2 class='subtitle'>Members</h2>   
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Username</th>
                            <th>Full name</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="member in team.members"
                            v-bind:key="member.id"
                        >
                            <td>{{ member.username }}</td>
                            <td>{{ member.first_name }} {{ member.last_name }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'

export default {
    name: 'Team',
    data(){
    return {
        team: {
            members: [],
            created_by: {},
            plan: [], 
            }
        }
    },
    mounted(){
        this.getTeam()
    },
    methods: {
        async getTeam(){
            this.$store.commit('setIsLoading', true)
            
            axios
            .get('/api/v1/teams/get_my_team')
            .then(response => {
                this.team = response.data
                console.log(response.data)
            })
            // this.$router.push({name:'MyAccount'})
    
            .catch(error => {
                console.log(error)
            })
        this.$store.commit('setIsLoading', false)

        }
    }

}
</script>