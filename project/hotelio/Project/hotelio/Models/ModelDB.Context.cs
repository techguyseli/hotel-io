﻿//------------------------------------------------------------------------------
// <auto-generated>
//    This code was generated from a template.
//
//    Manual changes to this file may cause unexpected behavior in your application.
//    Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace hotelio.Models
{
    using System;
    using System.Data.Entity;
    using System.Data.Entity.Infrastructure;
    
    public partial class hotelioEntities : DbContext
    {
        public hotelioEntities()
            : base("name=hotelioEntities")
        {
        }
    
        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            throw new UnintentionalCodeFirstException();
        }
    
        public DbSet<city> cities { get; set; }
        public DbSet<comment> comments { get; set; }
        public DbSet<hotel> hotels { get; set; }
        public DbSet<ml_testing_data> ml_testing_data { get; set; }
        public DbSet<ml_training_data> ml_training_data { get; set; }
        public DbSet<option> options { get; set; }
        public DbSet<reservation> reservations { get; set; }
        public DbSet<room> rooms { get; set; }
        public DbSet<rooms_reservation> rooms_reservation { get; set; }
        public DbSet<user> users { get; set; }
    }
}
