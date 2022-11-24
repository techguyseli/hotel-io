namespace hotelio.Models
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    public partial class User
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public User()
        {
            Commentaires = new HashSet<Commentaire>();
            Reservations = new HashSet<Reservation>();
        }

        [Key]
        public int idUser { get; set; }

        [Required]
        [StringLength(20)]
        public string email { get; set; }

        [Required]
        [StringLength(200)]
        public string mdp { get; set; }

        [Required]
        [StringLength(15)]
        public string nom { get; set; }

        [Required]
        [StringLength(30)]
        public string prenom { get; set; }

        [Required]
        [StringLength(50)]
        public string adresse { get; set; }

        [Required]
        [StringLength(15)]
        public string numTel { get; set; }

        [Required]
        [StringLength(15)]
        public string userRole { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<Commentaire> Commentaires { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<Reservation> Reservations { get; set; }
    }
}
