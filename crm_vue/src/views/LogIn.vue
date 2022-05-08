<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log in</h1>
            
                <form @submit.prevent='submitForm'> <!--to .prevent the default actions of html to be called -->
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" name="email" class="input" v-model="username"> <!-- v-model will change the data base on the input  
                            example user enter 'shiva' in username the data will also changed to shiva -- see the return data below -->  
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="password">
                        </div>
                    </div>
                    <div class='notification is-danger' v-if='errors.length'> <!--Check if there are errors -->
                        <p v-for='error in errors' v-bind:key='error' >{{error}}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>    
</template>

<script>
import axios from 'axios'

import {toast} from 'bulma-toast'

export default {
    name: 'LogIn',
    data() {
        return{
        username: '',
        password: '',
        errors: []
        }
    },
    methods: {
        async submitForm(){ //async means before we send it to the server 

            this.$store.commit('setIsLoading',true)
            axios.defaults.headers.common['Authorization'] = '' //reset the authorization to know we are not authentcated
            localStorage.removeItem('token') 
        
            const formData = {
                username: this.username, 
                password: this.password 
            }

            await axios 
            .post('/api/v1/token/login/', formData)
            .then(response => {
                const token = response.data.auth_token 

                this.$store.commit('setToken', token)

                axios.defaults.headers.common['Authorization'] = 'Token ' + token

                localStorage.setItem('token', token)

                this.$router.push('/dashboard/my-account') 
            })
            .catch(error => {
            if (error.response){
                for(const property in error.response.data){
                    this.errors.push(`${property}: ${error.response.data[property]}`)
                }
            } else if (error.message){
                this.errors.push('Something went wrong. Please try again')
                }
            })

            await axios //we wanted to store the data id and username of the user in vuex store
            .get('api/v1/users/me') 
            .then(response =>{
                this.$store.commit('setUser',{'id':response.data.id,'username':response.data.username}) //change value or add value in setUSer

                localStorage.setItem('username', response.data.username)
                localStorage.setItem('userid',response.data.id )


            }),
            await axios
            .get('api/v1/teams/get_my_team')
            .then(response => {
                // console.log(response.data)
                this.$store.commit('setTeam',{
                    'id':response.data.id,
                    'name':response.data.name,
                    'plan':response.data.plan.name,
                    'max_leads':response.data.plan.max_leads,
                    'max_clients':response.data.plan.max_clients})
                this.$router.push('/dashboard/my-account') 
                

            })
            .catch(error => {
                console.log(error)
            })
            this.$store.commit('setIsLoading',false)

        }   
    }
}
</script>   