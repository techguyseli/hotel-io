using System;
using System.ComponentModel.DataAnnotations.Schema;
using System.Data.Entity;
using System.Linq;

namespace hotelio.Models
{
    public partial class MVCHotelioModel : DbContext
    {
        public MVCHotelioModel()
            : base("name=MVCHotelioModel")
        {
        }

        public virtual DbSet<Chambre> Chambres { get; set; }
        public virtual DbSet<ChambresReservee> ChambresReservees { get; set; }
        public virtual DbSet<Commentaire> Commentaires { get; set; }
        public virtual DbSet<Hotel> Hotels { get; set; }
        public virtual DbSet<Option> Options { get; set; }
        public virtual DbSet<Reservation> Reservations { get; set; }
        public virtual DbSet<sysdiagram> sysdiagrams { get; set; }
        public virtual DbSet<User> Users { get; set; }
        public virtual DbSet<Ville> Villes { get; set; }

        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Chambre>()
                .Property(e => e.typeChambre)
                .IsUnicode(false);

            modelBuilder.Entity<Commentaire>()
                .Property(e => e.Commentaire1)
                .IsUnicode(false);

            modelBuilder.Entity<Hotel>()
                .Property(e => e.nom)
                .IsUnicode(false);

            modelBuilder.Entity<Hotel>()
                .Property(e => e.rib)
                .IsUnicode(false);

            modelBuilder.Entity<Hotel>()
                .HasMany(e => e.Chambres)
                .WithOptional(e => e.Hotel)
                .WillCascadeOnDelete();

            modelBuilder.Entity<Hotel>()
                .HasMany(e => e.Commentaires)
                .WithOptional(e => e.Hotel)
                .WillCascadeOnDelete();

            modelBuilder.Entity<Hotel>()
                .HasMany(e => e.Options)
                .WithMany(e => e.Hotels)
                .Map(m => m.ToTable("HotelOptions").MapLeftKey("idHotel").MapRightKey("idOption"));

            modelBuilder.Entity<Option>()
                .Property(e => e.HotelOption)
                .IsUnicode(false);

            modelBuilder.Entity<Reservation>()
                .Property(e => e.resevationStatut)
                .IsUnicode(false);

            modelBuilder.Entity<User>()
                .Property(e => e.email)
                .IsUnicode(false);

            modelBuilder.Entity<User>()
                .Property(e => e.mdp)
                .IsUnicode(false);

            modelBuilder.Entity<User>()
                .Property(e => e.nom)
                .IsUnicode(false);

            modelBuilder.Entity<User>()
                .Property(e => e.prenom)
                .IsUnicode(false);

            modelBuilder.Entity<User>()
                .Property(e => e.adresse)
                .IsUnicode(false);

            modelBuilder.Entity<User>()
                .Property(e => e.numTel)
                .IsUnicode(false);

            modelBuilder.Entity<User>()
                .Property(e => e.userRole)
                .IsUnicode(false);

            modelBuilder.Entity<User>()
                .HasMany(e => e.Reservations)
                .WithOptional(e => e.User)
                .WillCascadeOnDelete();

            modelBuilder.Entity<Ville>()
                .Property(e => e.nomVille)
                .IsUnicode(false);
        }
    }
}
